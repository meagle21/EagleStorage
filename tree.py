

class ParentNode:

    def __init__(self, s3_data):
        self.PARENT = s3_data['ParentFolder']
        self.CHILDREN = []
        self.NODE_NAME = s3_data['Name']
        self.NUM_CHILDREN = 0
        self.FILE_TYPE = s3_data['FileType']
    
    def get_parent(self):
        return self.PARENT
    
    def add_child(self, child_node):
        self.CHILDREN.append(child_node)
        self.NUM_CHILDREN += 1
    
    def get_children(self):
        return self.CHILDREN
    
    def get_node_name(self):
        return self.NODE_NAME
    
    def get_num_children(self):
        return self.NUM_CHILDREN
    
    def get_file_type(self):
        return self.FILE_TYPE

class ChildNode:

    def __init__(self, s3_data):
        self.NODE_NAME = s3_data["Name"]
        self.PARENT = s3_data["ParentFolder"]
        self.LAST_MODIFIED = s3_data["LastModified"]
        self.FILE_TYPE = s3_data["FileType"]
    
    def get_node_name(self):
        return self.NODE_NAME
    
    def get_parent(self):
        return self.PARENT
    
    def get_last_modified(self):
        return self.LAST_MODIFIED
    
    def get_file_type(self):
        return self.FILE_TYPE
    
    


