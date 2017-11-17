#!/bin/bash
# sistema - script que mostra informações sobre o sistema
# Autor: Ricardo Roberto de Lima

# Pede uma confirmação do usuário antes de executar
echo "Lendo os dados do Arquivo XMI. Posso continuar? [sn] "
read RESPOSTA

echo "Realizando as Transformacoes entre os modelos"
sleep 2
echo "[PIM]-Fazendo as tranformações para o [PSM] Django Python"
sleep 4
echo "Aplicando as mudanças no settings.py...."
sleep 5
echo "Aplicando as transformações no models.py..."
sleep 6
echo "Finalizando transformações..."
sleep 7
echo "Pronto para Executar"

# Se ele digitou 'n', vamos interromper o script
test "$RESPOSTA" = "n" && exit

# O date mostra a data e a hora correntes
echo "Data e Horário:"
date
echo

# O df mostra as partições e quanto cada uma ocupa no disco
echo "Uso do disco:"
df
echo

# O w mostra os usuários que estão conectados nesta máquina
echo "Usuários conectados:"
w

python manage.py runserver


