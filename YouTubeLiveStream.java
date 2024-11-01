import java.io.IOException;
public class YouTubeLiveStream {
    public static void main(String[] args) {
        // YouTube RTMP URL with your stream key
        String streamKey = "ea44-mwp4-e8g1-sxu5-0ryr"; // Replace with your actual YouTube stream key
        String rtmpUrl = "rtmp://a.rtmp.youtube.com/live2/" + streamKey;

        // FFmpeg command for continuous streaming
        String command = String.format(
                "ffmpeg -re -stream_loop -1 -i ./HanumanChalisa.mp4 -c:v libx264 -preset veryfast -maxrate 3000k " +
                "-bufsize 6000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 128k -ar 44100 -f flv %s",
                rtmpUrl
        );

        // Execute the FFmpeg command using Java ProcessBuilder
        try {
            ProcessBuilder processBuilder = new ProcessBuilder("sh", "-c", command);
            processBuilder.redirectErrorStream(true);
            Process process = processBuilder.start();

            System.out.println("Streaming to YouTube Live... Press Ctrl+C to stop.");

            // Output any error messages from FFmpeg
            process.getErrorStream().transferTo(System.out);
            process.waitFor();
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
