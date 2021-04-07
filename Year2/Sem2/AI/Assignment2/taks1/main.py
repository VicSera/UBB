from taks1.domain.dmap import Map
from taks1.gui.gui import GUI
from taks1.service.search_service import SearchService

# define a main function
def main():
    service = SearchService()
    gui = GUI(service)
    gui.run()

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
