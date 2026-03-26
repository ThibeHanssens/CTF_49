<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
Osint escape

Category:
Osing


Hints, info:
When you find the location of the dr, you are one step away from the flag. I hope you can xort this out


Files:
Kasm container

Problem description:
        This is an OSINT, escape game, challenge. Run the following Docker command on your laptop to run a kasm container (ask help from a coach if you are not familiar). The container will be available at https://localhost:6901. Remember to open a command prompt and type "start". You should see the background change (and other things will be configured). Use this environment to solve the challenge and find the flag!



        Username: kasm_user ; password: password



        docker run --rm -it --shm-size=512m -p 6901:6901 -e VNC_PW=password tclhowest/egypt:2

</pre>


### Write-up:
The challenge begins inside the Kasm container, where an email from Dr. Sophia Langley contains a password-protected ZIP file and instructions for decryption.


#### First part of the password
Following the leads in the email sent by Dr. Sophia Langley I found the "Jorge Amaro" profile on google after searching for a while I made the conclusion that Jorge had nothing to do with it and it all had to do with the "canabis" mentioned in the email canabis day is 4-20 I think the first part is 4-20.

This didn't seem to work so I went back to the google maps location "Sahara Pyramids Inn" and checked the specific images of that company. When I went to the 360 images I found the image she was talking about. The clock indeed shows 4-2 so that means 04:10 Dr. Sophia stated that the password format is hh-mm-Name

The first part definitely is 04-10

#### Second part of the password
For the second part there is a paper where coffee spilled over with login details but in FBI fashion you are able to select the text and login to the site no problem, when logging into that site you are able to read their co-writen paper. In the email Dr.Sophia mentions "Itsuwari no kami" when reading through that paper I didn't find a direct link to "Itsuwari no kami" which means false god in Japanese. But when I look up "Gnosticism false god" I find info about "Yaldabaoth" I decided to just try it and test that as the second part of the password

It worked and now i can view the attachements

#### The attachements
There were 2 files attached:
- An image
- A data file

The hint was that when you reach that dir you should xort it out. I need to xor the data file to get the actual datafile.

When checking out the image provided in the attachement it is a grid with letters on it. This links directly to the research paper where "the path to the treasure" is the same grid. When following that path on the attached image you get the word "GREATSPHINX" when xor'ing the data file with that as the key in UTF-8 you get the correct file.

chmoding the file so it is an executable and running it returns the ctf flag

