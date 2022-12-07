cat <<EOF>kasa-pump.sh
#!/bin/bash
if [[ ! -z $1 ]]; then
  operation=$1
else
  operation=state
fi
export PATH=/home/pi/.local/bin:$PATH
kasa --type plug --alias "water pump" ${operation}
EOF
