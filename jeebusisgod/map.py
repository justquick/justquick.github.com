from glob import glob
import os
import re


SU = [os.path.basename(x) for x in glob('index_files/*.gif')]
r = {}
PU = [os.path.basename(x).replace('.txt.html', '') for x in glob('html/*')]
for p in PU:
    for s in SU:
        if re.search('.*%s.*' % p.upper(), s.upper()):
            r[p] = s
r['deut'] = 'DueteronomyBlue.gif'

OT = ('genesis', 'exodus', 'levit', 'numbers', 'deut', 'joshua', 'judges', 'ruth', '1samuel', '2samuel', '1kings', '2kings', '1chron', '2chron', 'ezra', 'nehemiah', 'esther', 'job', 'psalms',
      'proverbs', 'eccl', 'song', 'isaiah', 'jeremiah', 'lament', 'ezekiel', 'daniel', 'hosea', 'joel', 'amos', 'obadiah', 'jonah', 'micah', 'nahum', 'habakkuk', 'zeph', 'haggai', 'zech', 'malachi',)
NT = ('matthew', 'mark', 'luke',  'john', 'acts', 'romans', '1corinth', '2corinth', 'galatian', 'ephesian', 'philipp', 'colossia', '1thess', '2thess',
      '1timothy', '2timothy', 'titus', 'philemon', 'hebrews',  'james', '1peter', '2peter', '1john',      '2john',    '3john',   'jude',         'rev', )
lut = {'levit': 'Leviticus', 'deut': 'Dueteronomy', '1chron': 'First Chronicles', '2chron': 'Second Chronicles', 'eccl': 'Ecclesiastes', 'song': 'Song of Solomon', 'lament': 'Lamentations',
       'zeph': 'Zephaniah', 'zech': 'Zechariah', '1corinth': 'First Corinthians', '2corith': 'Second Corinthians', '1thes': 'First Thessalonians', '2thes': 'Second Thessalonians', 'rev': 'Revelation'}
nums = {'1': 'First', '2': 'Second', '3': 'Third'}


def title(k):
    if k in lut.keys():
        return lut[k]
    elif k[0] in list('123'):
        return nums[k[0]]+' '+k[1].upper()+k[2:]
    else:
        return k[0].upper()+k[1:]


def imgs(k):
    return r[k]
