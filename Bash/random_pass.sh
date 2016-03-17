##gera senha com 8 caracteres
dd if=/dev/random ibs=6 count=1 2>/dev/null | mimencode
