import java.util.*;
import java.io.*;

public class Erase
{
	static void erase(String full, String home) throws Exception
	{
		Scanner in = new Scanner(new File(full));
		PrintWriter out = new PrintWriter(home);
		
		while (in.hasNextLine()) {
			String line = in.nextLine();
			if (!line.contains("@")) {
				out.println(line);
			}
		}
		out.close();
	}
	
	public static void main(String[] args) throws Exception
	{
		for (int i = 0; i < args.length; i++) {
			String filename = args[i];
			String fileNoExt = filename.split("\\.")[0];
			erase(filename, fileNoExt+"home.csv");
		}
	}
}