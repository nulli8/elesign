echo Hello $(whoami). Initializing elesign...
mkdir signed-ipas
touch signed-ipas/.gitkeep
sudo chmod +x elesign
echo Initialized. 
rm init.sh