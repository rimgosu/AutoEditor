import subprocess

ts_files = ['matsuri 2nomi barden.ts', 'matsuri 4kalec togg.ts', 'matsuri demon yogg.ts', \
    'matsuri dlchang yori.ts', 'matsuri galywix goldenbran.ts', 'matsuri joiackseok.ts', \
        'matsuri noz dlchang jangro.ts', 'matsuri omu cook.ts', 'matsuri reno demon.ts', 'matsuri teotar rakanishue.ts']

for ts_file in ts_files:
    output_file = ts_file.replace('.ts', '.mp4')
    subprocess.run(['ffmpeg', '-i', ts_file, output_file])