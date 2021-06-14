// get current directory using os library
package main

import (
	"fmt"
	"os"
)

func main() {
 
    pwd, err := os.Getwd()
    if err != nil {
        fmt.Println("Error:", err)
    }
    
    fileinfo, err := os.Lstat(pwd)
    
    fmt.Println(fileinfo.Name())
    fmt.Println(fileinfo.IsDir())

}
