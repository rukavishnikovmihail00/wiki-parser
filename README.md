# How to run

- docker login -u `username` -p `password`
- chmod +x run.sh
- ./run.sh `username`  
for example:
`./run.sh rukavishnikovmihail00`

# Ho to start the app
- docker pull `username`/wiki-parser:latest
- docker run -it --rm -v `your_folder`/:/app/result/ `username`/wiki-parser:latest `title` `lang`  
for example:
`docker run -it --rm -v "$(pwd)"/:/app/result/ rukavishnikovmihail00/wiki-parser:latest "Docker_(software)" "en" `