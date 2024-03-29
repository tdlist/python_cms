"""empty message

Revision ID: 4f8c2ac6e124
Revises: b7e23ef81504
Create Date: 2020-12-18 10:50:00.919828

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
from app.constants import ResourceEnum, Operation

# revision identifiers, used by Alembic.
revision = '4f8c2ac6e124'
down_revision = 'b7e23ef81504'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dat_resource_permission',
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True, comment='创建日期'),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True, comment='更新日期'),
    sa.Column('resource_permission_id', sa.Integer(), autoincrement=True, nullable=False, comment='资源权限配置id'),
    sa.Column('resource_id', sa.Integer(), nullable=False, comment='资源id'),
    sa.Column('permission_id', sa.Integer(), nullable=False, comment='权限id'),
    sa.Column('created_by', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_robot', sa.Integer(), nullable=True, comment='负责创建的机器人'),
    sa.Column('updated_by', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_robot', sa.Integer(), nullable=True, comment='负责更新的机器人'),
    sa.PrimaryKeyConstraint('resource_permission_id'),
    comment='资源权限配置表'
    )
    op.create_index(op.f('ix_dat_resource_permission_create_robot'), 'dat_resource_permission', ['create_robot'], unique=False)
    op.create_index(op.f('ix_dat_resource_permission_created_at'), 'dat_resource_permission', ['created_at'], unique=False)
    op.create_index(op.f('ix_dat_resource_permission_created_by'), 'dat_resource_permission', ['created_by'], unique=False)
    op.create_index(op.f('ix_dat_resource_permission_update_robot'), 'dat_resource_permission', ['update_robot'], unique=False)
    op.create_index(op.f('ix_dat_resource_permission_updated_at'), 'dat_resource_permission', ['updated_at'], unique=False)
    op.create_index(op.f('ix_dat_resource_permission_updated_by'), 'dat_resource_permission', ['updated_by'], unique=False)
    op.create_table('sys_resource',
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True, comment='创建日期'),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True, comment='更新日期'),
    sa.Column('resource_id', sa.Integer(), autoincrement=True, nullable=False, comment='资源id'),
    sa.Column('resource_name', sa.String(length=30), nullable=False, comment='权限名称'),
    sa.Column('resource_description', sa.String(length=50), nullable=True, comment='资源描述'),
    sa.Column('created_by', sa.Integer(), nullable=True, comment='创建人'),
    sa.Column('create_robot', sa.Integer(), nullable=True, comment='负责创建的机器人'),
    sa.Column('updated_by', sa.Integer(), nullable=True, comment='更新人'),
    sa.Column('update_robot', sa.Integer(), nullable=True, comment='负责更新的机器人'),
    sa.PrimaryKeyConstraint('resource_id'),
    sa.UniqueConstraint('resource_name'),
    comment='资源表'
    )
    op.create_index(op.f('ix_sys_resource_create_robot'), 'sys_resource', ['create_robot'], unique=False)
    op.create_index(op.f('ix_sys_resource_created_at'), 'sys_resource', ['created_at'], unique=False)
    op.create_index(op.f('ix_sys_resource_created_by'), 'sys_resource', ['created_by'], unique=False)
    op.create_index(op.f('ix_sys_resource_update_robot'), 'sys_resource', ['update_robot'], unique=False)
    op.create_index(op.f('ix_sys_resource_updated_at'), 'sys_resource', ['updated_at'], unique=False)
    op.create_index(op.f('ix_sys_resource_updated_by'), 'sys_resource', ['updated_by'], unique=False)
    op.alter_column('dat_declaration', 'returns_path',
               existing_type=mysql.JSON(),
               comment='文件存储位置',
               existing_nullable=True)
    op.add_column('dat_role_permission', sa.Column('resource_permission_id', sa.Integer(), nullable=False, comment='权限id'))
    op.drop_column('dat_role_permission', 'permission_id')
    # ### end Alembic commands ###
    for item in ResourceEnum.__members__.values():
        op.execute(
            f'insert into sys_resource (resource_name, created_by) values ("{item.name}", 0);')
    for item in Operation.__members__.values():
        op.execute(
            f'insert into sys_permission (permission_name, created_by) values ("{item.name}", 0);')


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dat_role_permission', sa.Column('permission_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False, comment='权限id'))
    op.drop_column('dat_role_permission', 'resource_permission_id')
    op.alter_column('dat_declaration', 'returns_path',
               existing_type=mysql.JSON(),
               comment=None,
               existing_comment='文件存储位置',
               existing_nullable=True)
    op.drop_index(op.f('ix_sys_resource_updated_by'), table_name='sys_resource')
    op.drop_index(op.f('ix_sys_resource_updated_at'), table_name='sys_resource')
    op.drop_index(op.f('ix_sys_resource_update_robot'), table_name='sys_resource')
    op.drop_index(op.f('ix_sys_resource_created_by'), table_name='sys_resource')
    op.drop_index(op.f('ix_sys_resource_created_at'), table_name='sys_resource')
    op.drop_index(op.f('ix_sys_resource_create_robot'), table_name='sys_resource')
    op.drop_table('sys_resource')
    op.drop_index(op.f('ix_dat_resource_permission_updated_by'), table_name='dat_resource_permission')
    op.drop_index(op.f('ix_dat_resource_permission_updated_at'), table_name='dat_resource_permission')
    op.drop_index(op.f('ix_dat_resource_permission_update_robot'), table_name='dat_resource_permission')
    op.drop_index(op.f('ix_dat_resource_permission_created_by'), table_name='dat_resource_permission')
    op.drop_index(op.f('ix_dat_resource_permission_created_at'), table_name='dat_resource_permission')
    op.drop_index(op.f('ix_dat_resource_permission_create_robot'), table_name='dat_resource_permission')
    op.drop_table('dat_resource_permission')
    # ### end Alembic commands ###
