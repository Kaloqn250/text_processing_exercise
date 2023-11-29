file_path = input().split('\\')
file_extension = file_path[-1].split('.')

print(f'File name: {file_extension[0]}\nFile extension: {file_extension[1]}')
