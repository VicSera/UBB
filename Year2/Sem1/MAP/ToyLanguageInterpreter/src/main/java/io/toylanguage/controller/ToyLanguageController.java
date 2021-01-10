package io.toylanguage.controller;

import io.toylanguage.datastructure.Heap;
import io.toylanguage.datastructure.Stack;
import io.toylanguage.datastructure.aliases.TypeEnvironment;
import io.toylanguage.exception.ToyLanguageException;
import io.toylanguage.logger.Logger;
import io.toylanguage.model.ProgramState;
import io.toylanguage.model.statement.Statement;
import io.toylanguage.model.value.Value;
import io.toylanguage.model.value.implementation.RefValue;
import io.toylanguage.repository.ProgramStateRepository;

import java.util.*;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

public class ToyLanguageController {
    ProgramStateRepository programStateRepository;
    private final Logger logger = new Logger();
    ExecutorService executor;

    public ToyLanguageController(ProgramStateRepository programStateRepository) {
        this.programStateRepository = programStateRepository;
        executor = Executors.newFixedThreadPool(3);
    }

    public List<ProgramState> getPrograms() {
        return programStateRepository.getPrograms();
    }

    public void execute() throws ToyLanguageException {
        executor = Executors.newFixedThreadPool(3);

        List<ProgramState> programs = removeFinishedPrograms(programStateRepository.getPrograms());
        while (!programs.isEmpty()) {
            garbageCollector(
                    getAddressesFromSymbolTable(combineSymbolTableValues(programs)),
                    programs.get(0).getHeap()
            );

            try {
                stepWithEachProgram(programs);
            } catch (InterruptedException exception) {
                exception.printStackTrace();
            }
            programs = removeFinishedPrograms(programStateRepository.getPrograms());
        }

        executor.shutdownNow();

        programStateRepository.setPrograms(programs);
    }

    public void oneStep() {
        List<ProgramState> programs = removeFinishedPrograms(programStateRepository.getPrograms());
        programStateRepository.setPrograms(programs);
        garbageCollector(
                getAddressesFromSymbolTable(combineSymbolTableValues(programs)),
                programs.get(0).getHeap()
        );

        try {
            stepWithEachProgram(programs);
        } catch (InterruptedException exception) {
            exception.printStackTrace();
        }

    }

    private void stepWithEachProgram(List<ProgramState> programs) throws InterruptedException {
        List<Callable<ProgramState>> callList = programs.stream()
                .map((ProgramState program) -> (Callable<ProgramState>) program::step)
                .collect(Collectors.toList());

        List<ProgramState> threads = executor.invokeAll(callList).stream()
                .map(futureCall -> {
                    try {
                        return futureCall.get();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    } catch (ExecutionException e) {
                        System.out.println(e.getCause().getMessage());
                    }
                    return null;
                })
                .filter(Objects::nonNull)
                .collect(Collectors.toList());

        programs.addAll(threads);
        programs.forEach(thread -> {
            try {
                programStateRepository.logProgramState(thread);
            } catch (ToyLanguageException exception) {
                System.out.println(exception.getMessage());
            }
        });

        programStateRepository.setPrograms(programs);
    }

    private List<ProgramState> removeFinishedPrograms(List<ProgramState> programs) {
        return programs.stream()
                .filter(program -> !program.isFinished())
                .collect(Collectors.toList());
    }

    private void garbageCollector(List<Integer> symbolTableAddresses, Heap heap) {
        List<Integer> heapAddresses = heap.values()
                .stream()
                .filter(value -> value instanceof RefValue)
                .map(value -> ((RefValue) value).getAddress())
                .collect(Collectors.toList());

        heap.setContent(
                heap.entrySet()
                        .stream()
                        .filter(e ->
                                symbolTableAddresses.contains(e.getKey()) || heapAddresses.contains(e.getKey()))
                        .collect(Collectors.toMap(
                                Map.Entry<Integer, Value>::getKey,
                                Map.Entry<Integer, Value>::getValue))
        );
    }

    private Collection<Value> combineSymbolTableValues(List<ProgramState> programs) {
        return programs.stream()
                .map(ProgramState::getSymbolTable)
                .flatMap(symbolTable -> symbolTable.values().stream())
                .collect(Collectors.toList());

    }

    private List<Integer> getAddressesFromSymbolTable(Collection<Value> symbolTableValues) {
        return symbolTableValues
                .stream()
                .filter(v -> v instanceof RefValue)
                .map(v -> {
                    RefValue refValue = (RefValue) v;
                    return refValue.getAddress();
                }).collect(Collectors.toList());
    }
}
