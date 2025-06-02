from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process
import os
from time import perf_counter
from PIL import Image, ImageFilter

filenames = [
    "images/1.jpg",
    "images/2.jpg",
    "images/3.jpg",
    "images/4.jpg",
    "images/5.jpg",
]

def thumbnail(filename: str, size=(50,50), thumb_dir="thumbs"):
    # Open the image
    img = Image.open(filename)
    # Apply the gaussian blur filter
    img = img.filter(ImageFilter.GaussianBlur)
    # create a thumbnail
    img.thumbnail(size)
    # Save the image
    img.save(f"{thumb_dir}/{os.path.basename(filename)}")
    # Display a message
    print(f"{filename=} was processed...")

if __name__ == "__main__":
    start = perf_counter()
    
    # Create processes
    processes = [Process(target=thumbnail, args=[filename]) for filename in filenames]
    # Start the processes
    [p.start() for p in processes]
    # Wait for completion
    [p.join() for p in processes]

    with ProcessPoolExecutor() as executor:
        executor.map(thumbnail, filenames)
        
    # for name in filenames:
    #     thumbnail(name)
    end = perf_counter()

    print(f"Duration: {end-start:.2f}s")
