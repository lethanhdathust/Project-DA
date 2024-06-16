package exercise1_2;

import java.io.*;
import java.util.Scanner;

class    MainMenu {

    
        public static void menuReadAndWrite() {
            System.out.println("\t\t*******************************************");
            System.out.println("\n\nPress 1 : To write text file");
            System.out.println("Press 2 : To Read text file");
            System.out.println("Press 3 : To write binary file ");
            System.out.println("Press 4 : To Read binary file");
            System.out.println("Press 5 : To Read file info");
            System.out.println("Press 6 : To get Current Project Path");
            System.out.println("Press 7 : To create Folder");
            System.out.println("Press 8 : To listed The File And Folder In A Folder");

            System.out.println("Press 10 : To  exit ");


        }
    }
    
public class ReadAndWrite {

    public static void readTextFile() {
        File file = new File("exercise1_2/readText.txt");
        try {
            BufferedReader br = new BufferedReader(new FileReader(file));
            String line;
            while ((line = br.readLine())!= null) {
                System.out.println(line);
            }
            br.close();
        }
        catch(IOException e){

            e.printStackTrace();

        }
    }

    public static void writeTextFile() {
        // Create a new file
        File file = new File("exercise1_2/writeFile.txt");
        try {

            BufferedWriter writer = new BufferedWriter(new FileWriter(file));
            writer.write("hello my name is ....");
            writer.newLine();
            writer.write("end");
            writer.close();
            // sc.close();

        } catch (IOException e) {

            // TODO Auto-generated catch block
            e.printStackTrace();
        }

    }
    public static void writeBinaryFile() {
        // Create a new file
        File file = new File("exercise1_2/writeBinaryFile.bin");
        try (FileOutputStream write = new FileOutputStream(file)) {
            String content = "binary file content  rereerreer";
            write.write(content.getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
    public static void readBinaryFile() {
        // Create a new file
        File file = new File("exercise1_2/writeBinaryFile.bin");
        try (FileInputStream read = new FileInputStream(file)) {
            int line;
//            line = ;
            while((line = read.read())!=-1){
                System.out.print(line + " ");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
    public static void fileInfo(){
        File file = new File("/home/dell/Downloads/624.jpg");
        // Check if the file exists
        System.out.println("Path exists : " + file.exists());
        if(file.exists()){
//            Check ìf it is a folder or not
            System.out.println("isDirectory : " + file.isDirectory());
// Get the name
            System.out.println("Name: " + file.getName());
//Get the size of file
            System.out.println("Length : " + file.length() );
        }
    }
    public static void createFolder()
    {
        File dir = new File("/home/dell/Downloads/newTest");
        System.out.println("Pathname: " + dir.getAbsolutePath());
        System.out.println("Path exists:  " + dir.exists());
        System.out.println("Parent Path: " + dir.getParentFile()); // false
        // create the new folder if the parent's folder exists, if the folder exists we cannot create
        boolean created = dir.mkdir();
        System.out.println("Directory created: " + created); // false

    }
    public static void getCurrentProjectPath(){
        File file = new File("");
        String currentPath = file.getAbsolutePath();
        System.out.println("Current Project Path"+ currentPath);
    }
    public static void listedTheFileAndFolderInAFolder(){
        System.out.println(" List files and folder in a folder: ");
        File dir = new File("/home/dell/Documents/training-in-cty/tuan1");
        File[] children = dir.listFiles();
        if (children != null) {
            for (File file : children) {
                System.out.println(file.getAbsolutePath());
            }
        }

        System.out.println();

        System.out.println("List the name of file and folder: ");
        String[] paths = dir.list();
        if (paths != null) {
            for (String path : paths) {
                System.out.println(path);
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        MainMenu.menuReadAndWrite();
         int i = 0;
        while(i < 10){
            i = sc.nextInt();
            switch (i) {
                case 1:
                    sc.nextLine();
                    writeTextFile();
                    break;
                case 2:
                    readTextFile();
                    break;
                case 3:
                    writeBinaryFile();
                    break;
                case 4:
                    readBinaryFile();
                    break;
                case 5:
                    fileInfo();
                    break;
                case 6:
                    getCurrentProjectPath();
                    break;
                case 7:
                    createFolder();
                    break;
                case 8:
                    listedTheFileAndFolderInAFolder();
                default:
                    break;
            }
        }
sc.close();
    }
   
}