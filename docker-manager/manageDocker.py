import subprocess

def get_docker_images():
    try:
        # Run the "docker image list" command and capture the output
        result = subprocess.run("docker image list", shell=True, capture_output=True, text=True, check=True)

        # The output of the command is stored in the 'stdout' attribute of the 'result' object
        docker_images_output = result.stdout

        # Split the input string into lines and skip the header line
        lines = docker_images_output.strip().split('\n')[1:]

        # Create a list to store image details
        docker_images = []

        # Iterate through the lines and create objects for each image
        for line in lines:
            parts = line.split()
            image_id = parts[2]  # Image ID is at index 2
            repository = parts[0]
            created = parts[4] + " " + parts[5]  # Combine the "CREATED" and "TIME AGO" columns
            size = parts[6]

            # Create a dictionary for each image and add it to the list
            docker_image = {
                "IMAGE ID": image_id,
                "REPOSITORY": repository,
                "CREATED": created,
                "SIZE": size
            }
            docker_images.append(docker_image)

        return docker_images
    except subprocess.CalledProcessError as e:
        print("Error:", e)

def check_images_usage(image_list):
    image_status = {}

    for image in image_list:
        image_id = image["IMAGE ID"]
        is_used = is_image_in_use(image_id)
        image_status[image_id] = is_used

    return image_status

def is_image_in_use(image_id):
    try:
        subprocess.run(f"docker inspect {image_id}", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True  # Image exists and can be inspected, so it's in use
    except subprocess.CalledProcessError as e:
        return False  # Image does not exist, so it's not in use

def delete_docker_image(image_id):
    try:
        subprocess.run(f"docker rmi -f {image_id}", shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return False
