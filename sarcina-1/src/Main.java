import org.w3c.dom.css.RGBColor;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedImage img = ImageIO.read(new FileInputStream("src/best.bmp"));
        int[] pixels = img.getRGB(0, 0, img.getWidth(), img.getHeight(), null, 0, img.getWidth());

        int pixelSum = 0;
        for(int pixel : pixels) {
            if (pixel < -3795200 / 2)
                pixelSum++;
        }

        System.out.println(pixelSum);

    }
}
