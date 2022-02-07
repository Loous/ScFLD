import os.path
import os
import sys
import pathlib
import shutil


class SearchFl:
    def __init__(self):
        
        self._options = sys.argv
        
        
    def Menu(self):
        if len(self._options) > 1:
        
            option = sys.argv[1]
            
            if option == "-fd":
                self.filesFD()
                
            elif option == "-p":     
                self.filesP()
                
            else:
                print("La opción ingresada no se encuentra disponible")
                
        else:
            print("No se han ingresado los párametros necesarios")
            
            
    def filesFD(self):
        """
        
        -fd cambiar todos los archivos a un nuevo directorio
            -r nuevo directorio
            -t tipo de archivo suffix .txt, .exe, etc
            
            example -fd [path] -t [.txt] -r [new path]
        
        """
        
        self._options.remove("searchFL.py")
        
        if len(self._options) == 6:
            
            opath = self._options[1]
            suffix = self._options[3]
            nwpath = self._options[5]
            
            if os.path.exists(opath) and os.path.exists(nwpath):
            
                x = os.listdir(opath)
                
                files = []
                
                for n in x:
                    if suffix in n:
                        files.append(n)
                        
                    else:
                        continue
                    
                if len(files) == 0:
                    print(f"\nNo se encontro ningún archivo con el sufijo '{suffix}'")
                    
                else:
                        
                    filesPath = []
                        
                    for n2 in files:
                        filesPath.append(os.path.join(opath, n2))
                        
                    
                    for n3 in filesPath:
                        try:
                        
                            shutil.move(n3, nwpath)
                            
                        except shutil.Error:
                            x = pathlib.PurePath(n3)
                            
                            print(f"El archivo {x.parts[-1]} ya existe en el nuevo directorio")
                             
                            
                    print("\nArchivos cambiados con éxito")
                    
                    
            else:
                print("\nLas rutas ingresadas no son válidas")
                    
        else:
            print("\nDebes ingresar los parametros necesarios")
            
            
    
                              
    def filesP(self):
        """
        -p buscar archivos con los permisos especificados.
            -r busca los archivos con permiso de lectura.
            -w busca los archivos con permiso de escritura.
            -x busca los archivos con permiso ejecutable.
            -rwx busca los archivos con todos los permisos.
            
            Ejemplo: -p [path] -f
            
        
        """
        
        if len(self._options) == 4:
        
            options = ["-r", "-w", "-x", "-rwx"]
            
            
            path = self._options[2]
            option = self._options[3]
            
            if os.path.exists(path) and option in options:
                files = os.listdir(path)
                    
                            
                if option == "-r":
                    self.filesPValidation(path, files, os.R_OK, "Lectura")
                    
                            
                            
                elif option == "-w":
                    self.filesPValidation(path, files, os.W_OK, "Escritura")
                            
                            
                elif option == "-x":
                    self.filesPValidation(path, files, os.X_OK, "Ejecución")
                            
                            
                elif option == "-rwx":
                    filesFRWX = []
                    
                    for n in files:
                        x = os.path.join(path, n)
                    
                        if os.access(x, os.R_OK) and os.access(x, os.W_OK) and os.access(x, os.X_OK):
                            filesFRWX.append(x)
                            
                    if len(filesFRWX) == 0:
                        print("No se encontraron archivos con todos los permisos")
                            
                    else:
                        for n2 in filesFRWX:
                            print(f"archivo con todos los permisos: {n2}")
                            
            else:
                print("La ruta u opción especificada es incorrecta")
                
        else:
            print("No se ingresaron los párametros necesarios")
                            
        
    def filesPValidation(self, path, files, permision, tipo):
        
        filesP = []
                    
        for n in files:
            x = os.path.join(path, n)
                        
            if(os.access(x, permision)):
                filesP.append(x)
                
                            
        if len(filesP) == 0:
            print(f"No se encontraron archivos con permisos de {tipo}")
                        
        else:
            for n2 in filesP:
                print(f"archivo con permisos de {tipo}: {pathlib.PurePath(n2).name}")
                
                
        
if __name__ == "__main__":
    SearchFl().Menu()
        
        
        
        
        
        
        