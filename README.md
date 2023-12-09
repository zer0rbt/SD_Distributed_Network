# Stable Diffusion Distributed Network

**Version:** v0.1

**ATTENTION:** *WORK IN PROGRESS*

## What is it?

Distributed computations network, dedicated to allowing faster image generation speed. It also contains features like a distributed database. This project is created as part of the "Distributed Computations" course at SPbU.

## Build

`docker build -t deps -f ./Dockerfile .` (можно загрузить готовый из dockerhub v131v/sd-deps)

`docker build -t stablediffusion ./stablediffusion/.`

`docker build -t upscaler ./upscalers/.`

`docker build -t database ./database/.`

## Usage

`docker run -it --rm --name rabbitmq -h rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management` - запуск rabbitmq с админкой на порту 15672

`docker run --name sd1 -v ./:/workspace/cache -v ./models/:/workspace/models --env-file ./.env --network host --rm stablediffusion` - запуск sd service
./ - заменить на путь для временного хранения картинок
./models - заменить на путь до моделей
./.env - заменить на путь до .env файла

`docker run --name up1 -v ./:/workspace/cache -v ./models/:/workspace/models --env-file ./.env --network host --rm upscaler` - запуск upscaler service
./ - заменить на путь для временного хранения картинок
./models - заменить на путь до моделей
./.env - заменить на путь до .env файла

`docker run --name database1 -v ./:/workspace/storage --env-file ./.env -p 5003:5003 --rm database` - запуск database service на порту 5003
./ - заменить на путь для хранения картинок
./.env - заменить на путь до .env файла

## TODO LIST

### First Priority (minimum required version)

- [x] Image generator (v0.1)
- [x] Image upscaler (v0.1)
- [x] Image storage (v0.1)
- [x] Server (v0.0.1)

### Second priority (optimal version)

- [ ] Message Broker (To Do)
- [ ] Logger (To Do)
- [ ] Log Storage (To Do)

### Third priority (minimum required final version)

- [ ] Load Balancer (To Do)

### Fourth priority (optimal final version)

- [ ] OpenVPN clusters (To Do)
- [ ] Config storage (To Do)

## Contributors

- **zer0rbt** - idea & code
- **v113v** - architecture & code (we hope so :^])
