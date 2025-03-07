import os
import subprocess

def merge_segments(segment_files, output_file):
    # FFmpeg'in concat demuxer'ı için geçici bir liste dosyası oluşturuyoruz.
    list_file = "segments.txt"
    with open(list_file, "w", encoding="utf-8") as f:
        for segment in segment_files:
            # FFmpeg'in isteği: her satır "file 'tam_yol'" şeklinde olmalı.
            abs_path = os.path.abspath(segment)
            f.write(f"file '{abs_path}'\n")
    
    # FFmpeg komutunu çalıştırıyoruz:
    # -f concat : concat demuxer'ı kullan.
    # -safe 0   : mutlak yolları kabul eder.
    # -i list_file : oluşturduğumuz liste dosyasını input olarak ver.
    # -c copy : yeniden kodlama yapmadan doğrudan birleştir.
    cmd = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", list_file,
        "-c", "copy",
        output_file
    ]
    
    print("FFmpeg ile birleştirme başlatılıyor...")
    subprocess.run(cmd)
    
    # Geçici liste dosyasını siliyoruz.
    os.remove(list_file)
    print(f"Videolar başarıyla birleştirildi: {output_file}")

if __name__ == "__main__":
    # Birleştirmek istediğiniz segmentlerin dosya isimlerini doğru sırayla ekleyin.
    segment_files = [f"segment_{i}.ts" for i in range(10000)]

    output_file = "merged_video.mp4"
    merge_segments(segment_files, output_file)
