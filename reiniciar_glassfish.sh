#!/bin/bash

# Reinicia Glassfish en modo debug, quitando todas las aplicaciones
# desplegadas.
# Es necesario configurar la variable ASADMIN con la ruta del ejecutable
# asadmin de Glassfish.

ASADMIN=~/.local/bin/glassfish3/bin/asadmin

function reiniciar_glassfish {
	echo ''
	echo '-------------------------------------------------------'
	echo 'Undeploying all...'
	echo '-------------------------------------------------------'
	for p in $*; do
		echo "Undeploying $p..."
		$ASADMIN undeploy $p
	done;

	echo ''
	echo '-------------------------------------------------------'
	echo 'Reiniciando Glassfish...'
	echo '-------------------------------------------------------'
	$ASADMIN stop-domain -t
	$ASADMIN start-domain --debug -t
}

aplicaciones=`$ASADMIN list-applications -t | awk '{print $1;}'`

reiniciar_glassfish $aplicaciones
echo ''
echo '-------------------------------------------------------'
echo 'Listo.'
echo '-------------------------------------------------------'
echo ''
