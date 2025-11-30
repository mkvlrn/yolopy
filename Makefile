.PHONY: dev build

dev:
	@uv run src/main.py

build:
	@rm -rf ./bin
	@pyinstaller -F src/main.py --distpath ./bin --specpath ./build -n yolo
