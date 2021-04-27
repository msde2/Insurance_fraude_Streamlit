mkdir -p ~/.streamlit/
echo "\
[general]
email = \"faical.Aitlahbib@live.fr\"
" > ~/.streamlit/credentials.toml
echo "\
[server]
headless = true
enableCORS=false
port = $PORT
" > ~/.streamlit/config.toml
