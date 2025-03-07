import os
import requests
import m3u8
import zipfile

def download_segments(m3u8_url, output_folder):
    # m3u8 playlist dosyasını yükle
    playlist = m3u8.load(m3u8_url)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    segment_files = []
    for i, segment in enumerate(playlist.segments):
        # Segment URL'si; bazı durumlarda absolute_uri kullanmanız gerekebilir
        seg_url = segment.absolute_uri if segment.absolute_uri else segment.uri
        output_file = os.path.join(output_folder, f"segment_{i}.ts")
        print(f"{i + 1}. segment indiriliyor: {seg_url}")

        try:
            response = requests.get(seg_url, stream=True)
            response.raise_for_status()
            with open(output_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            segment_files.append(output_file)
            print(f"Segment {i + 1} başarıyla indirildi: {output_file}")
        except requests.exceptions.RequestException as e:
            print(f"Segment {i + 1} indirilirken hata: {e}")
    return segment_files

def compress_files_to_zip(file_list, zip_file_name):
    try:
        with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zf:
            for file_path in file_list:
                zf.write(file_path, os.path.basename(file_path))
        print(f"Tüm dosyalar {zip_file_name} olarak sıkıştırıldı.")
    except Exception as e:
        print(f"Zip oluşturulurken hata: {e}")

if __name__ == "__main__":
    # m3u8 playlist URL'sini buraya girin
    m3u8_url = "https://vz-08281008-c21.b-cdn.net/8f95e30d-7a31-48a0-abc3-910801013e09/720p/video.m3u8"  # Gerçek URL ile değiştirin
    output_folder = "segments"  # Segmentlerin kaydedileceği klasör
    zip_file_name = "linux.zip"  # Çıkış zip dosyası adı

    # Tüm segmentleri indir
    segment_files = download_segments(m3u8_url, output_folder)
    
    # İndirilen segmentleri zip dosyası içinde sıkıştır
    if segment_files:
        compress_files_to_zip(segment_files, zip_file_name)
    else:
        print("Hiç segment indirilemedi.")
