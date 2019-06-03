.PHONY: default
default: package

.PHONY: package
package:
	python3 setup.py --quiet sdist

.PHONY: publish
publish:
	@echo "Publishing pyadb internally"
	twine upload -r pyadb $(shell ls -tr ./dist/* | sort -r | head)

.PHONY: clean
clean:
	rm -rf ./dist/ ./MAINFEST
