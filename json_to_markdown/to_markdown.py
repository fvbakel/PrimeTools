#
# Convert the Primes json output to markdown

import json
import os
import json
from datetime import datetime
import pandas as pd


class prime_parser:

    def process_json(file_name):
        f = open(file_name)
        
        # returns JSON object as 
        # a dictionary
        data = json.load(f)

        df_results = pd.json_normalize(data['results'])
        df_cpu = pd.json_normalize(data['machine']['cpu'])
        df_os = pd.json_normalize(data['machine']['os'])
        df_docker = pd.json_normalize(data['machine']['docker'])
        df_system = pd.json_normalize(data['machine']['system'])

        df_results.rename(columns={"tags.algorithm": "algorithm", "tags.faithful": "faithful", "tags.bits": "bits","tags.parallel":"parallel"},inplace=True)
        df_results['passes per sec'] = df_results.passes / df_results.duration
       
        out_file=file_name.replace('.json','.md')
        with open(out_file, 'w') as output:
            output.write('# Prime results\n\n')
            output.write('Report date in UTC: %s\n\n' % (datetime.utcfromtimestamp(data['metadata']['date']).strftime('%Y-%m-%d %H:%M:%S')))

            output.write('1. [Top 10 single threaded](#top-10-single-threaded)\n')
            output.write('2. [Top 10 multi threaded](#top-10-multi-threaded)\n')
            output.write('3. [All results](#all-results)\n')
            output.write('4. [Test details](#test-details)\n')
            output.write('\n')
            cols = df_results.columns.tolist()
            cols=  cols[:3] + cols[-1:] + cols[3:-1]

            ## Top 10 single threaded\n\n')

            output.write('### Base, Faithful, 1 thread, 1 bit\n\n')
            tmp_df = df_results[ \
                (df_results['faithful']=='yes') & \
                (df_results['algorithm']=='base') & \
                (df_results['bits']=='1') & \
                (df_results['threads']==1)][cols].sort_values(by=['passes per sec'], \
                ascending=False).head(10).reset_index(drop=True)
            tmp_df.index = tmp_df.index +1
            tmp = tmp_df.to_markdown(index=True)
            output.write(tmp)
            output.write('\n')

            output.write('### Not wheel, Faithful, 1 thread\n\n')
            tmp_df = df_results[ \
                (df_results['faithful']=='yes') & \
                (df_results['algorithm']!='wheel') & \
            #    (df_results['bits']=='1') & \
                (df_results['threads']==1)][cols].sort_values(by=['passes per sec'], \
                ascending=False).head(10).reset_index(drop=True)
            tmp_df.index = tmp_df.index +1
            tmp = tmp_df.to_markdown(index=True)
            output.write(tmp)
            output.write('\n')

            output.write('### Faithful, 1 thread\n\n')
            tmp_df = df_results[ \
                (df_results['faithful']=='yes') & \
                (df_results['algorithm']=='base') & \
            #    (df_results['bits']=='1') & \
                (df_results['threads']==1)][cols].sort_values(by=['passes per sec'], \
                ascending=False).head(10).reset_index(drop=True)
            tmp_df.index = tmp_df.index +1
            tmp = tmp_df.to_markdown(index=True)
            output.write(tmp)
            output.write('\n')

            output.write('### Single threaded\n\n')
            tmp_df = df_results[ \
            #    (df_results['faithful']=='yes') & \
            #    (df_results['algorithm']=='base') & \
            #    (df_results['bits']=='1') & \
                (df_results['threads']==1)][cols].sort_values(by=['passes per sec'], \
                ascending=False).head(10).reset_index(drop=True)
            tmp_df.index = tmp_df.index +1
            tmp = tmp_df.to_markdown(index=True)
            output.write(tmp)
            output.write('\n')


            output.write('## Top 10 multi threaded\n\n')

            output.write('### Base, Faithful, multi thread, 1 bit\n\n')
            tmp_df = df_results[ \
                (df_results['faithful']=='yes') & \
                (df_results['algorithm']=='base') & \
                (df_results['bits']=='1') & \
                (df_results['threads']!=1)][cols].sort_values(by=['passes per sec'], \
                ascending=False).head(10).reset_index(drop=True)
            tmp_df.index = tmp_df.index +1
            tmp = tmp_df.to_markdown(index=True)
            output.write(tmp)
            output.write('\n')

            output.write('### Not wheel, Faithful, multi thread\n\n')
            tmp_df = df_results[ \
                (df_results['faithful']=='yes') & \
                (df_results['algorithm']!='wheel') & \
            #    (df_results['bits']=='1') & \
                (df_results['threads']!=1)][cols].sort_values(by=['passes per sec'], \
                ascending=False).head(10).reset_index(drop=True)
            tmp_df.index = tmp_df.index +1
            tmp = tmp_df.to_markdown(index=True)
            output.write(tmp)
            output.write('\n')

            output.write('### Faithful, multi thread\n\n')
            tmp_df = df_results[ \
                (df_results['faithful']=='yes') & \
                (df_results['algorithm']=='base') & \
            #    (df_results['bits']=='1') & \
                (df_results['threads']!=1)][cols].sort_values(by=['passes per sec'], \
                ascending=False).head(10).reset_index(drop=True)
            tmp_df.index = tmp_df.index +1
            tmp = tmp_df.to_markdown(index=True)
            output.write(tmp)
            output.write('\n')

            output.write('### Multi threaded\n\n')
            tmp_df = df_results[ \
            #    (df_results['faithful']=='yes') & \
            #    (df_results['algorithm']=='base') & \
            #    (df_results['bits']=='1') & \
                 (df_results['threads']!=1)][cols].sort_values(by=['passes per sec'], \
                ascending=False).head(10).reset_index(drop=True)
            tmp_df.index = tmp_df.index +1
            tmp = tmp_df.to_markdown(index=True)
            output.write(tmp)
            output.write('\n')

            output.write('## All results\n\n')
            #tmp = df_results[cols].sort_values(by=['passes per sec'], \
            #    ascending=False,ignore_index=True).head(10).reset_index(drop=True).to_markdown() #.reset_index(drop=True)
            tmp_df = df_results[cols].sort_values(by=['passes per sec'], \
                ascending=False).reset_index(drop=True)
            tmp_df.index = tmp_df.index +1
            tmp = tmp_df.to_markdown(index=True)
            output.write(tmp)
            output.write('\n')

            output.write('\n## Test details\n\n')

            output.write('\n### Cpu\n\n')
            tmp_df = df_cpu.T
            tmp_df.columns = ['Value']
            tmp = tmp_df[tmp_df.index!='flags'].to_markdown()
            output.write(tmp)
            output.write('\n\n')

            tmp_df = df_cpu.T
            tmp_df.columns = ['Value']
            tmp = tmp_df.filter(like='flags', axis=0).to_markdown()
            output.write(tmp)
            output.write('\n')

            output.write('\n### OS\n\n')
            tmp_df = df_os.T
            tmp_df.columns = ['Value']
            tmp = tmp_df.to_markdown()
            output.write(tmp)
            output.write('\n')

            output.write('\n### System\n\n')
            tmp_df = df_system.T
            tmp_df.columns = ['Value']
            tmp = tmp_df.to_markdown()
            output.write(tmp)
            output.write('\n')

            output.write('\n## Docker\n\n')
            tmp_df = df_docker.T
            tmp_df.columns = ['Value']
            tmp = tmp_df.to_markdown()
            output.write(tmp)
            output.write('\n')
            
        

    
    def process_dir(dir_name):
        directory = os.fsencode(dir_name)
            
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".json"): 
                fullname = os.path.join(dir_name, filename)
                prime_parser.process_json(fullname)

prime_parser.process_dir('/data')

