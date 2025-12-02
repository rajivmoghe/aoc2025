import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class Day01 {
    public static void main(String[] args) {
        Path filepath = Paths.get("/home/rajiv/projects/adventofcode/aoc2025/day01/small");

        try{
            List<String> list = Files.readAllLines(filepath);
            int count = 0;
            int start = 50;
            for(String line:list)
            {
                //System.out.println(line);

                String letter = line.replaceAll("[0-9]", "");
                int digits = Integer.parseInt(line.replaceAll("[^0-9]", ""));


                if (letter.equals("L")) {
                    start = (start - digits + 100) % 100;
                } else if(letter.equals("R")){
                    start = (start + digits) % 100;
                }

                if(start == 0)
                    count++;


            }
            System.out.println(count);

        }catch (Exception e)
        {
            System.out.println("Error reading file "+e);
        }

    }
}