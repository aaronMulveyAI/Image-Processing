import cv2

# Ruta de la imagen
ruta_imagen = "images/bananas.JPG"

try:
    # Carga la imagen
    bananos = cv2.imread(ruta_imagen)


    # Verifica si la imagen se cargó correctamente
    if bananos is None:
        raise FileNotFoundError(f"Error: La imagen no se pudo cargar. Verifica la ruta: {ruta_imagen}")



    # Muestra la imagen original
    cv2.imshow("Imagen Original", bananos)

    # Divide la imagen en sus canales (B, G, R)
    canales = {
        "Canal Azul": bananos[:, :, 0],  # Canal azul
        "Canal Verde": bananos[:, :, 1],  # Canal verde
        "Canal Rojo": bananos[:, :, 2]   # Canal rojo
    }
    
    # Muestra los canales por separado
    for nombre, canal in canales.items():
        cv2.imshow(nombre, canal)

    # Espera a que se presione cualquier tecla para cerrar las ventanas
    print("Presiona cualquier tecla en la ventana para cerrar.")
    cv2.waitKey(0)

except FileNotFoundError as e:
    print(e)

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

finally:
    # Cierra todas las ventanas de OpenCV
    cv2.destroyAllWindows()
