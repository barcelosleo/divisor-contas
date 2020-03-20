all: cls compile_views compile_resources

run: cls compile_resources compile_views
	fbs run

cls:
	clear

compile_views: ./src/main/python/UI/*.ui
	for file_name in $(basename $^); do \
		pyuic5 --resource-suffix='' --import-from=. --resource-suffix='Resources' --output=$(basename $${file_name}).py $${file_name}.ui ; \
	done

compile_resources: ./src/main/python/UI/*.qrc
	for file_name in $(basename $^); do \
		pyrcc5 -o $(basename $${file_name})Resources.py $${file_name}.qrc; \
	done