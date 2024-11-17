install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff
