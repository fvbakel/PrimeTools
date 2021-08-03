import numpy as np
from PIL import Image, ImageDraw
import cv2
from math import sqrt
from math import floor
import os
   
class PrimeSieveVideo:
    data_dir = "/data"
    OFF = (255, 255, 255)
    ON = (0, 0, 0)
    
    prime_counts = { 10 : 4,
                100 : 25,
                1000 : 168,
                10000 : 1229,
                100000 : 9592,
                1000000 : 78498,
                10000000 : 664579,
                100000000 : 5761455
    }

    def __init__(self,nr_of_skip_frames,limit):
        self._nr_of_skip_frames = nr_of_skip_frames
        self._size = limit
        self._bitsize = limit / 2
        self._sqrt = floor(sqrt(self._bitsize))
        
        videodims = (self._sqrt+2,self._sqrt +1)
        frames_per_sec = 10
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self._video = cv2.VideoWriter( PrimeSieveVideo.data_dir + os.sep + "limit-" + str(limit) + ".mp4",fourcc, frames_per_sec,videodims)
        self._image = Image.new('RGB', videodims, color = 'black')
        self.write_frame()
        self._pixels = self._image.load()
        self._frame_nr = 0
    
    def write_frame(self):
        self._video.write(cv2.cvtColor(np.array(self._image), cv2.COLOR_RGB2BGR))
        
    def get_bit(self,index):
        col = index // self._sqrt
        row = index % self._sqrt
        return self._pixels[col,row]
    
    def clear_bit(self,index):
        col = index // self._sqrt
        row = index % self._sqrt
        
        self._frame_nr = self._frame_nr +1
        if self._frame_nr > self._nr_of_skip_frames:
            self._frame_nr = 0
            self.write_frame()
        
        self._pixels[col,row] = PrimeSieveVideo.OFF
    
    def print_results(self):
        count = self.count_primes()
        valid = self.validate_results(count)
        print("Limit: %i, Found: %i, Valid: %s" % (self._size,count,valid))
    
    def validate_results(self,count):
        if self._size in self.prime_counts:  
            return PrimeSieveVideo.prime_counts[self._size] == count
        return False
    
    def count_primes(self):
        count = 1
        i = 1
        while i<self._bitsize:
            if self.get_bit(i) == PrimeSieveVideo.ON:
                count = count + 1
            i = i + 1
        return count
    
    def run_sieve(self):

        factor = 1
  
        while factor <= self._sqrt:
            
            if self.get_bit(factor) == PrimeSieveVideo.ON:
                prime = (factor *2) + 1
                start_index = floor(((prime * prime) -1)/2)
                
                i = start_index
                frame_i = 0
                while i<self._bitsize:
                    self.clear_bit(i)
                    i = i+ prime

            factor += 1
        
        self.write_frame()
        self._video.release()

if __name__ == "__main__":
    sieve = PrimeSieveVideo(5000,1000000)
    sieve.run_sieve()
    sieve.print_results()
        