The script can help you, if you have a lot of photos, and every name has digits in the end.
The script allows you to achieve the following goals:
- Put photos from different cameras into different folders.
- Rename the photos: change the word (the sequence name) and the sequence number (start from 1, add padding).
- Create a file with statistics
- Delete original files

Requirements:
- MS Windows.
- Python 2.7.
- A folder with files (usually photos).
- Every file must have a name, consisting of two parts: (1) one or more non-digits and (2) one or more digits. For example: 'photo-12.jpg'
The second part will be converted as a number, so it must be unique for all files with the same first parts: 
you can't have both files with names like 'photo01' and 'photo1', because after the conversion '01' will be equal to '1'.
The second part after the conversion must be 1 or more, not 0.


How to use:
- Drag and drop the folder with all photos on the script.
- Enter new sequence names for each sequence in English or Russian.
- Answer, whether you want to delete the original files or not.


What is different from the example:
- It works for more than 1 sequence.
- The folder with photos isn't a part of the script.
- New sequence names aren't parts of the script.
- It creates a file with statistics.
- The name of the folder with photos can be not only in English, but in Russian too.
- Original names of the photos can be not only in English, but in Russian too.
- New names of the photos can be not only in English, but in Russian too.