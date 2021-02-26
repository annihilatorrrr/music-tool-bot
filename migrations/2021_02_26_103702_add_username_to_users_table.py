from orator.migrations import Migration


class AddUsernameToUsersTable(Migration):
    def up(self):
        with self.schema.table('users') as table:
            table.string('username').after('user_id').default('')

    def down(self):
        with self.schema.table('users') as table:
            table.drop_column('username')
