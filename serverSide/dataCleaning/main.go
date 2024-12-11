package main

import (
	"log"
	"os"
	"regexp"
)

func cleanFile(filename string) {
	fileContent, err := os.ReadFile(filename)

	cleanedContent := cleanContents(string(fileContent))

	if err != nil {
		log.Fatalf(err.Error())
	}

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
	dir, dirErr := os.ReadDir("receivedLogs")
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
