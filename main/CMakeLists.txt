idf_component_register(SRCS "main.c" "file_server.c" "mount.c"
                    INCLUDE_DIRS ".")

set(image ../fatfs_image)
fatfs_create_spiflash_image(storage ${image} FLASH_IN_PROJECT)
