cmake_minimum_required(VERSION 3.0)
PROJECT(Blinky C)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

enable_language(ASM)

set(EXECUTABLE_NAME Blinky.elf)

# MCU stuff
set(MCU CYBL11573-56LQXI)
set(FLASH_ROW_SIZE 256)
set(FLASH_SIZE 262144)
	
###############################
set(CMAKE_COLOR_MAKEFILE true)
set(CMAKE_VERBOSE_MAKEFILE OFF)

set(CMAKE_C_FLAGS "-std=gnu99 -mcpu=cortex-m0 -mthumb -Wno-main -Wall -ffunction-sections -ffat-lto-objects -D DEBUG")
set(CMAKE_EXE_LINKER_FLAGS "-Wl,--start-group -mcpu=cortex-m0 -mthumb -g -ffunction-sections -O1 -ffat-lto-objects -Wl,-Map,${EXECUTABLE_NAME}.map -T cm0gcc.ld -specs=nano.specs -Wl,--gc-sections -Wl,--end-group")
# ASM flags
set(CMAKE_CUSTOM_ASM_FLAGS "-mcpu=cortex-m0 -mthumb -I . -W")
set(CMAKE_ASM_FLAGS_DEBUG ${CMAKE_CUSTOM_ASM_FLAGS})
set(CMAKE_ASM_FLAGS_RELEASE ${CMAKE_CUSTOM_ASM_FLAGS})
set(CMAKE_ASM_FLAGS_MINSIZEREL ${CMAKE_CUSTOM_ASM_FLAGS})

#message("CMAKE_C_FLAGS_DEBUG is ${CMAKE_C_FLAGS_DEBUG}")
#message("CMAKE_C_FLAGS_RELEASE is ${CMAKE_C_FLAGS_RELEASE}")
#message("CMAKE_C_FLAGS_RELWITHDEBINFO is ${CMAKE_C_FLAGS_RELWITHDEBINFO}")
#message("CMAKE_C_FLAGS_MINSIZEREL is ${CMAKE_C_FLAGS_MINSIZEREL}")

# disable use of *ranlib after creating a lib
set(CMAKE_C_ARCHIVE_FINISH "" )
add_subdirectory(Generated_Source/PSoC4)

set(SRC_FILES
	main.c
)

include_directories(${PROJECT_SOURCE_DIR})
include_directories(${PROJECT_SOURCE_DIR}/Generated_Source/PSoC4)
link_directories(${PROJECT_SOURCE_DIR}/Generated_Source/PSoC4)

add_executable(${EXECUTABLE_NAME} ${PSOC_FILES} ${SRC_FILES})