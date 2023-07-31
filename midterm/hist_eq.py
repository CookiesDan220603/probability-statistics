import os, sys
import cv2
import numpy as np

try:
    import seaborn as sns
    import pandas as pd
except:
    raise Exception('Seaborn or Pandas packages not found. Installation: $ pip install seaborn pandas')
    
def create_histogram(img):
    assert len(img.shape) == 2 # check grayscale image
    histogram = [0] * 256 # list of intensity frequencies, 256 zero values
    for row in range(img.shape[0]): # traverse by row (y-axis)
        for col in range(img.shape[1]): # traverse by column (x-axis)
            histogram[img[row, col]] += 1
    return histogram

def visualize_histogram(histogram, output='histogram.png'):
    hist_data = pd.DataFrame({'intensity': list(range(256)), 'frequency': histogram})
    sns_hist = sns.barplot(x='intensity', y='frequency', data=hist_data, color='blue')
    sns_hist.set(xticks=[]) # hide x ticks
    
    fig = sns_hist.get_figure()
    fig.savefig(output)
    return output

def equalize_histogram(img, histogram):
    # build H', cumsum
    new_H = [0] * 257
    for i in range(0, len(new_H)):
        new_H[i] = sum(histogram[:i])
    new_H = new_H[1:]
       
    # normalize H'
    #max_H = max(new_H)
    #max_hist = max(histogram)
    #new_H = [(f/max_H)*max_hist for f in new_H]
    
    # scale H' to [0, 255]
    max_value = max(new_H)
    min_value = min(new_H)
    new_H = [int(((f-min_value)/(max_value-min_value))*255) for f in new_H]
    
    print("H':", new_H)
    
    # apply H' to img
    for row in range(img.shape[0]): # traverse by row (y-axis)
        for col in range(img.shape[1]): # traverse by column (x-axis)
            img[row, col] = new_H[img[row, col]]
    return img

if __name__ == "__main__":
    assert len(sys.argv) == 2, '[USAGE] $ python %s img_6.jpg' % (os.path.basename(__file__), INPUT)
    INPUT = sys.argv[1]
    assert os.path.isfile(INPUT), '%s not found' % INPUT
    
    # read color image with grayscale flag: "cv2.IMREAD_GRAYSCALE"
    img = cv2.imread(INPUT, cv2.IMREAD_GRAYSCALE)
    # print grayscale image
    cv2.imwrite('grey_%s' % INPUT, img)
    print('Saved grayscale image @ grey_%s' % INPUT)
    
    # create histogram from image
    histogram = create_histogram(img)
    print('histogram:', histogram)
    
    hist_img_path = visualize_histogram(histogram)
    print('Saved histogram @ %s' % hist_img_path)
    
    equalized_img = equalize_histogram(img, histogram)
    cv2.imwrite('equalized_%s' % INPUT, equalized_img)
    print('Saved equalized image @ equalized_%s' % INPUT)
    
    new_histogram = create_histogram(equalized_img)
    print('new_histogram:', new_histogram)
    hist_img_path = visualize_histogram(new_histogram, output='histogram_eq.png')
    print('Saved new histogram @ %s' % hist_img_path)
    
    print('Done Tut 6: Histogram Equalization. Welcome to minhng.info')