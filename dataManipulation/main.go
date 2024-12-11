package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strings"
)

func multispaceToSingleSpace(s string) string {
	multipleSpace := `\s+`
	pattern := regexp.MustCompile(multipleSpace)
	return pattern.ReplaceAllString(s, string(rune(32)))
}


func obtainEntryCred(s string) []string {
	singleSpacedEntry := multispaceToSingleSpace(s)

	entities := strings.Split(singleSpacedEntry, string(rune(32)))

	if len(entities) < 8{
		return nil
	}

	username := entities[0]
	logTime := entities[len(entities)-6:]

	return append([]string{username}, logTime...)
}


func main() {
	//attempt to open user.txt
	//forward slash dir, backslach escape
	userFile, err := os.ReadFile("dataManipulation/userLogFile/users.txt")

	//check for error
	if err != nil{
		log.Fatalf(err.Error())
	}

	//gives us lpgins as per lines of entry
	fileEntries := strings.Split(string(userFile), string(rune(10)))

	//figuring out whats innit per line
	// fmt.Println([]byte(fileEntries[4]))
	// -> planning to use regex exp to convert multispace to singlespace

	// -> success
	// fmt.Println([]byte(multispaceToSingleSpace(fileEntries[4])))

	// now to get username and logtime as a list
	fmt.Println(strings.Join(obtainEntryCred(fileEntries[4]), ","))

	f, errf := os.OpenFile("output/data.csv", os.O_CREATE | os.O_WRONLY, 0644)

	if errf != nil {
		log.Fatalf(errf.Error())
	}
	
	defer f.Close()

	for _, ch := range fileEntries{
		//saving our data to a csv file
		inputEntry := obtainEntryCred(ch)
		if inputEntry == nil{
			continue
		}

		_,writeErr := f.WriteString(strings.Join(inputEntry, ",") + string(rune(10)))

		if writeErr != nil{
			log.Fatalf(writeErr.Error())
		}
		
	}

	

	//fmt.Println(string(userFile))

}