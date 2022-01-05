import os
from more_itertools import chunked


class Bingo():

    def __init__(self, input_data):
        self.tables = []
        self.win_table = None
        self.shadow_tables = []
        self.entries = []

        data = input_data.split('\n')
        entries = data[0].rstrip().split(',')
        self.entries = [int(x) for x in entries]
        del(data[0])
        data = [d for d in data if d]
        data = list(chunked(data, 5))

        for line in data:
            table = []
            s_table = []
            for row in line:
                values_row = row.split(' ')
                table.append([int(v) for v in values_row if v])

            self.tables.append(table)

        for tbl in self.tables:
            table = [[0] * len(_) for _ in tbl]
            self.shadow_tables.append(table)
    
    def mark_shadow(self, entry):
        for tbl, table in enumerate(self.tables):
            for rw, row in enumerate(table):
                if entry in row:
                    col = row.index(entry)
                    self.shadow_tables[tbl][rw][col] = 1
    
    def run_entries(self, last=False):
        last_entry = None
        value = 0
        
        for entry in self.entries:
            self.mark_shadow(entry)
            if last:
              results = self.check_bingo(last=True, enrty=entry)
              
            else:
                if self.check_bingo():
                    last_entry = entry
                    break
        
        if self.win_table:
            for x,row in enumerate(self.shadow_tables[self.win_table]):
                for y,col in enumerate(row):
                    if not col:
                        value += self.tables[self.win_table][x][y]
            value = value * last_entry
            
        return value

    def check_bingo(self, last=False, enrty=None):
        tables_win = []
        
        for i,table in enumerate(self.shadow_tables):
            for row in table:
                if all(row):
                    if last:
                        tables_win.append([i,enrty])
                    else:
                        self.win_table = i
                        return True
                
            columns = [list(x) for x in zip(*table)]
            for col in columns:
                    if all(col):
                        if last:
                            tables_win.append([i, enrty])
                        else:
                            self.win_table = i
                            return True
        if last:
            import ipdb; ipdb.set_trace()
            return tables_win
        
        self.win_table = None
        return False


path = os.getcwd() + '/day4/input_data.txt'
input_data = open(path, 'r').read()
bingo = Bingo(input_data)
print(bingo.run_entries())
