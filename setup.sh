mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"tianyuan.zhang@epfedu.fr\"\n\
" > ~/.streamlit/credential.toml

 
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
                             