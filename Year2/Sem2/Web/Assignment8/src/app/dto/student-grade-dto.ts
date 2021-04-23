import {GradeDTO} from './grade-dto';

export interface StudentGradeDTO {
  id: number;
  username: string;
  grades: GradeDTO[];
}
