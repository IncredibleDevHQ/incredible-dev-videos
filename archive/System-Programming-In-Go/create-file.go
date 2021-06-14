// creating a new file in Go
package main

import (
    "fmt"
    "io/ioutil"
)

func main() {
    err := ioutil.WriteFile("my-file.txt", []byte("Hello"), 0755)
    if err != nil {
        fmt.Printf("Unable to write file: %v", err)
    }
}
