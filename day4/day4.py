import os
from typing import Counter
from more_itertools import chunked


class Bingo():

    def __init__(self, input_data):
        self.tables = []
        self.shadow_tables = []
        self.entries = []
        self.win_table = None

        data = input_data.split('\n')
        entries = data[0].rstrip().split(',')
        self.entries = [int(x) for x in entries]
        del(data[0])
        data = [d for d in data if d]
        data = list(chunked(data, 5))

        for line in data:
            table = []
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
    
    def run_entries(self):
        last_entry = None
        value = 0
        
        for entry in self.entries:
            self.mark_shadow(entry)
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
    
    def get_last_board(self):
        table_data = None
        value = 0
        
        for entry in self.entries:
            self.mark_shadow(entry)
            winers = self.check_bingo(first=False)
            print(winers)
                           
            #table_data = {
            #    'table': self.tables[self.win_table],
            #    'shadow': self.shadow_tables[self.win_table],
            #    'last_entry': entry
            #}
            #del(self.tables[self.win_table])
            #del(self.shadow_tables[self.win_table])
                
        import ipdb; ipdb.set_trace()
        for x, row in enumerate(table_data['shadow']):
                for y, col in enumerate(row):
                    if not col:
                        value += table_data['table'][x][y]
            
        value = value * table_data['last_entry']
        
        return value
    
    def check_bingo(self, first=True):
        if first:        
            for i,table in enumerate(self.shadow_tables):
                for row in table:
                    if all(row):
                            self.win_table = i
                            return True
                    
                columns = [list(x) for x in zip(*table)]
                for col in columns:
                        if all(col):
                                self.win_table = i
                                return True
                            
            self.win_table = None
            return False

        boards = []
        for i, table in enumerate(self.shadow_tables):
            for row in table:
                if all(row):
                    boards.append(self.tables[i])
            columns = [list(x) for x in zip(*table)]
            
            for col in columns:
                if all(row):
                    boards.append(self.tables[i])
        
        return boards


path = os.getcwd() + '/day4/input_data.txt'
input_data = open(path, 'r').read()
bingo = Bingo(input_data)
#print(bingo.run_entries())
print(bingo.get_last_board())
