from PIL import Image
def merging(img_path,chunk_size):
    img = Image.open(img_path)

    # Get the dimensions of the image
    width, height = img.size

    # Calculate the number of chunks in the x and y directions
    x_chunks = width // chunk_size
    y_chunks = height // chunk_size
    # Set the output image size (width and height)
    output_width = x_chunks * chunk_size
    output_height = y_chunks * chunk_size

    # Create a new output image with the correct size
    output_img = Image.new('RGB', (output_width, output_height))

    # Loop through each chunk and paste it into the output image
    for x in range(x_chunks):
        for y in range(y_chunks):
            # Open the chunk file
            chunk_filename = f'projectOC/powerlines-OC/output/chunk_{x}_{y}.jpg'
            chunk = Image.open(chunk_filename)

            # Calculate the coordinates to paste the chunk into the output image
            left = x * chunk_size
            upper = y * chunk_size
            right = (x + 1) * chunk_size
            lower = (y + 1) * chunk_size

            # Paste the chunk into the output image
            output_img.paste(chunk, (left,upper,right,lower))
    output_img.save('projectOC/powerlines-OC/output_image.jpg')
        
# Save the output image
#rotated_img = outplut_img.rotate(45)
merging('Timage.jpg',100)
