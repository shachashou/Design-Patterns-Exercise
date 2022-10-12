class Manager:
    successor = None
    name = ''

    def __init__(self, name):
        self.name = name

    def set_successor(self, successor):
        self.successor = successor

    def handle_request(self, request):
        pass


# 直属经理
class LineManager(Manager):
    def handle_request(self, request):
        if request.request_type == 'little':
            print('request_type: %s ,request_content: %s,' % (request.request_type, request.request_content))
            print('小事一桩，我这个小小的line manager就能搞定')
        else:
            if self.successor is not None:
                print('request_type: %s ,request_content: %s' % (request.request_type, request.request_content))
                print('非小事，我这个小小的line manager无能为力，交上级处理')
                print('上级是:', self.successor)
                self.successor.handle_request(request)


# 部门经理
class DepartmentManager(Manager):
    def handle_request(self, request):
        if request.request_type == 'middle':
            print('request_type: %s ,request_content: %s ' % (request.request_type, request.request_content))
            print('中级事件，我这个department manager就能搞定')
        else:
            if self.successor is not None:
                print('request_type: %s ,request_content: %s' % (request.request_type, request.request_content))
                print('非中级事件，我这个department manager无能为力，交上级处理')
                print('上级是:', self.successor)
                self.successor.handle_request(request)

    def __str__(self):
        return 'Department Manager '


# 总经理
class GeneralManager(Manager):
    def handle_request(self, request):
        if request.request_type == 'big':
            print('request_type: %s ,request_content: %s' % (request.request_type, request.request_content))
            print('大事件，得由我这个 general manager拍板')

    def __str__(self):
        return 'General Manager '


class Request:
    def __init__(self, request_type, request_content):
        self.request_type = request_type
        self.request_content = request_content

    def commit(self, manager):
        ret = manager.handle_request(self)


a = LineManager('Line Manager')
b = DepartmentManager('Department Manager')
c = GeneralManager('General Manager')
a.set_successor(b)
b.set_successor(c)

print('==========================================================')
r = Request('little', '请批准团队外出腐败经费1000元')
r.commit(a)

print('==========================================================')
r = Request('middle', '请批准团队外出旅游10000元')
r.commit(a)

print('==========================================================')
r = Request('big', '请批准团队设备购买100000元')
r.commit(a)
