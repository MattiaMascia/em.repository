def scrivi_paragrafi_in_file(file_path):
    testo = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec arcu in nisi elementum sollicitudin. Nullam a nisi vitae elit tempus mollis.
Quisque in tincidunt eros. Proin ac neque nisl. Phasellus faucibus sapien at auctor lobortis. Vivamus posuere orci id purus auctor dignissim.
Suspendisse potenti. Mauris viverra, lorem non suscipit tincidunt, odio erat lobortis sapien, vitae placerat felis augue in ligula."""
    
    with open(file_path, 'w') as file:
        file.write(testo)

# Chiamata alla funzione
scrivi_paragrafi_in_file('09-12/testo.txt')