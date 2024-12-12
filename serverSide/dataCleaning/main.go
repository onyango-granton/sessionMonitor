package main

import (
	"log"
	"os"
	"os/exec"
	"regexp"
)

func cleanFile(filename string) {
	fileContent, err := os.ReadFile("dataCleaning/receivedLogs/"+filename)

	cleanedContent := cleanContents(string(fileContent))

	if err != nil {
		log.Fatalf(err.Error())
	}

	checkIfDirExist("serverOutput")

	outputFile, outErr := os.OpenFile("serverOutput/"+filename, os.O_CREATE|os.O_WRONLY, 0644)
	if outErr != nil {
		log.Fatalf(outErr.Error())
	}

	_, writeErr := outputFile.Write([]byte(cleanedContent))

	if writeErr != nil {
		log.Fatalf(writeErr.Error())
	}

	outputFile.Close()
}

func cleanContents(content string) string {
	pattern := regexp.MustCompile(`\\+n`)
	return pattern.ReplaceAllString(content, string(rune(10)))
}

func readFromReceivedLogDir() {
	dir, dirErr := os.ReadDir("dataCleaning/receivedLogs")
	if dirErr != nil {
		log.Fatalf(dirErr.Error())
	}

	for _, file := range dir {
		cleanFile(file.Name())
	}
}

func main() {
	readFromReceivedLogDir()
}

/*checks if directory exists if not create one*/
func checkIfDirExist(directory string) {
	if _, dirErr := os.Stat(directory); os.IsNotExist(dirErr){
		cmd := exec.Command("mkdir", directory)
		if _, cmdErr := cmd.Output(); cmdErr != nil{
			log.Fatalf(cmdErr.Error())
		}
	}
}