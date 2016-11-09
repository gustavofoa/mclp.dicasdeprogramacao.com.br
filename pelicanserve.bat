pelican content --debug --autoreload  --output output --settings pelicanconf.py
pushd output
python -m pelican.server
popd
