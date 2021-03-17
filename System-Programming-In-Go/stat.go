// get file permission
package main

import (
	"fmt"
	"os"
)

func main() {
    pwd, err := os.Getwd()
    if err != nil {
        os.Exit(0)
    }

    info, err := os.Stat(pwd)
    if err != nil {
        os.Exit(0)
    }
    
    mode := info.Mode()
    fmt.Println("Permissions of the directory: ", mode)   
}
