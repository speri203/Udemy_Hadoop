from mrjob.job import MRJob
from mrjob.step import MRStep

class RatingsBreakdown(MRJob):

    def steps(self):
        return [MRStep(mapper= self.mapper_get_rating, 
                        reducer= self.reducer_count_rating)]
                        
    def mapper_get_rating(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield rating, 1

    def reducer_count_rating(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    RatingsBreakdown.run()