from mrjob.job import MRJob
from mrjob.step import MRStep

class Count_Ratings(MRJob):

    def step(self):
        return [MRStep(mapper= self.map_get_movies,
                reducer= self.reduce_get_movies),
                MRStep(reducer= self.reduce_count_movies)]
    
    def map_get_movies(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, 1
    
    def reduce_get_movies(self, key, value):
        yield str(sum(value)).zfill(5), key

    def reduce_count_movies(self, key, value):
        for movies in value:
            yield movies, key

if __name__ == '__main__':
    Count_Ratings.run()