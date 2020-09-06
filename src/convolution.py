import numpy as np

def convolution(image, kernal, weight = 1):
    image_processed = np.copy(image)

    size_x = image_processed.shape[0]
    size_y = image_processed.shape[1]


    for x in range(1, size_x-1):
        for y in range(1, size_y-1):
            output_pixel = 0.0
            output_pixel = output_pixel + (image[x - 1, y - 1] * kernal[0][0])
            output_pixel = output_pixel + (image[x, y-1] * kernal[0][1])
            output_pixel = output_pixel + (image[x + 1, y-1] * kernal[0][2])
            output_pixel = output_pixel + (image[x-1, y] * kernal[1][0])
            output_pixel = output_pixel + (image[x, y] * kernal[1][1])
            output_pixel = output_pixel + (image[x+1, y] * kernal[1][2])
            output_pixel = output_pixel + (image[x-1, y+1] * kernal[2][0])
            output_pixel = output_pixel + (image[x, y+1] * kernal[2][1])
            output_pixel = output_pixel + (image[x+1, y+1] * kernal[2][2])
            output_pixel = output_pixel * weight

            if(output_pixel<0):
                output_pixel=0
            if(output_pixel>255):
                output_pixel=255
            image_processed[x, y] = output_pixel
    return image_processed
